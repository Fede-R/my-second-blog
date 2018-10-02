; ; Rules for matching dishes with given preference
; ; Salience set to 1 so this rule will be fired at the end.
; ; (Other rules have salience = 2)
(defrule enfermedades-matching
	(declare (salience 1))
	(enfermedad (ID ?ID) (name ?name) (planta ?planta) (sintoma-aa ?sintomaAAA) (sintoma-bb ?sibb)			   
			(sintoma-cc ?sintomacc)
			(stars ?stars))
	(preference (planta "?"|?planta)
			(sintoma-aa "?"|?sintomaAAA)
			(sintoma-bb "?"|?sibb)
;;			(calorie-level "?"|?calorie)
;;			(fiber-level "?"|?fiber)
;;			(fat-level "?"|?fat)
;;			(carb-level "?"|?carb)
			(sintoma-cc "?"|?sintomacc))
;;			(sintoma-ee "?"|?sintomaee)
;;			(sour-level "?"|?sour)
;;			(sintoma-dd "?"|?sintomadd)
=>
	(printout t ?ID "," ?planta "," ?sintomaAAA "," ?sibb ","  
		?sintomacc "," ?stars "---")
)



; ; Rules for calculating dish rating from reviews
; ; Star will be != -1 after this rule.
(defrule enfermedads-rating
	(declare (salience 2))
	?d <- (enfermedad (ID ?id) (stars ?s&:(= ?s -1)))
=>
	(bind ?count 0)
	(bind ?sum 0)
	(do-for-all-facts
		((?r review))
		(= ?r:enfermedad-id ?id)
		(bind ?count (+ ?count 1))
		(bind ?sum (+ ?sum ?r:stars)))
	(if (> ?count 0)
		then
	(modify ?d (stars (/ ?sum ?count)))
		else
	(modify ?d (stars 0)))
)


; ; Rules for tuning the dishes basing on user's suggestions
; ; Rule of tuning "sintoma-bb"
(defrule tuning-sintoma-bb
	(declare (salience 2))
	?d <- (enfermedad (ID ?id) (sintoma-bb ?origin))
	(suggestion (enfermedad-id ?id) (attribute "sintoma-bb") (value ?value&:(neq ?value ?origin)) (quantity ?quantity))
	(not (suggestion (enfermedad-id ?id) (attribute "sintoma-bb") (value ?value2) 
		(quantity ?quantity2&:(or (> ?quantity2 ?quantity)(and (= ?quantity2 ?quantity) (< (str-compare ?value2 ?value) 0))))))
=>
	(modify ?d (sintoma-bb ?value))
)

; ; Rule of tuning "sintoma-aa"
(defrule tuning-sintoma-aa
	(declare (salience 2))
	?d <- (enfermedad (ID ?id) (sintoma-aa ?origin))
	(suggestion (enfermedad-id ?id) (attribute "sintoma-aa") (value ?value&:(neq ?value ?origin)) (quantity ?quantity))
	(not (suggestion (enfermedad-id ?id) (attribute "sintoma-aa") (value ?value2) 
		(quantity ?quantity2&:(or (> ?quantity2 ?quantity)(and (= ?quantity2 ?quantity) (< (str-compare ?value2 ?value) 0))))))

=>
	(modify ?d (sintoma-aa ?value))
)

; ; Rule of tuning "sintoma-cc"
(defrule tuning-sintoma-cc
	(declare (salience 2))
	?d <- (enfermedad (ID ?id) (sintoma-cc ?origin))
	(suggestion (enfermedad-id ?id) (attribute "sintoma-cc") (value ?value&:(neq ?value ?origin)) (quantity ?quantity))
	(not (suggestion (enfermedad-id ?id) (attribute "sintoma-cc") (value ?value2) 
		(quantity ?quantity2&:(or (> ?quantity2 ?quantity)(and (= ?quantity2 ?quantity) (< (str-compare ?value2 ?value) 0))))))
=>
	(modify ?d (sintoma-cc ?value))
)

; ; Rule of tuning "sour-level"
;;(defrule tuning-sour-level
;;	(declare (salience 2))
;;	?d <- (dish (ID ?id) (sour-level ?origin))
;;	(suggestion (dish-id ?id) (attribute "sour-level") (value ?value&:(neq ?value ?origin)) (quantity ?quantity))
;;	(not (suggestion (dish-id ?id) (attribute "sour-level") (value ?value2) 
;;		(quantity ?quantity2&:(or (> ?quantity2 ?quantity)(and (= ?quantity2 ?quantity) (< (str-compare ?value2 ?value) 0))))))
;;=>
;;	(modify ?d (sour-level ?value))
;;)

; ; Rule of tuning "sintoma-dd"
;;(defrule tuning-sintoma-dd
;;	(declare (salience 2))
;;	?d <- (enfermedad (ID ?id) (sintoma-dd ?origin))
;;	(suggestion (enfermedad-id ?id) (attribute "sintoma-dd") (value ?value&:(neq ?value ?origin)) (quantity ?quantity))
;;	(not (suggestion (enfermedad-id ?id) (attribute "sintoma-dd") (value ?value2) 
;;		(quantity ?quantity2&:(or (> ?quantity2 ?quantity)(and (= ?quantity2 ?quantity) (< (str-compare ?value2 ?value) 0))))))
;;=>
;;	(modify ?d (sintoma-dd ?value))
;;)

; ; Rule of tuning "sintoma-ee"
;;(defrule tuning-sintoma-ee
;;	(declare (salience 2))
;;	?d <- (enfermedad (ID ?id) (sintoma-ee ?origin))
;;	(suggestion (enfermedad-id ?id) (attribute "sintoma-ee") (value ?value&:(neq ?value ?origin)) (quantity ?quantity))
;;	(not (suggestion (enfermedad-id ?id) (attribute "sintoma-ee") (value ?value2) 
;;		(quantity ?quantity2&:(or (> ?quantity2 ?quantity)(and (= ?quantity2 ?quantity) (< (str-compare ?value2 ?value) 0))))))
;;=>
;;	(modify ?d (sintoma-ee ?value))
;;)

; ; Rule of tuning "fat-level"
;;(defrule tuning-fat-level
;;	(declare (salience 2))
;;	?d <- (dish (ID ?id) (fat-level ?origin))
;;	(suggestion (dish-id ?id) (attribute "fat-level") (value ?value&:(neq ?value ?origin)) (quantity ?quantity))
;;	(not (suggestion (dish-id ?id) (attribute "fat-level") (value ?value2) 
;;		(quantity ?quantity2&:(or (> ?quantity2 ?quantity)(and (= ?quantity2 ?quantity) (< (str-compare ?value2 ?value) 0))))))
;;=>
;;	(modify ?d (fat-level ?value))
;;)

; ; Rule of tuning "calorie-level"
;;(defrule tuning-calorie-level
;;	(declare (salience 2))
;;	?d <- (dish (ID ?id) (calorie-level ?origin))
;;	(suggestion (dish-id ?id) (attribute "calorie-level") (value ?value&:(neq ?value ?origin)) (quantity ?quantity))
;;	(not (suggestion (dish-id ?id) (attribute "calorie-level") (value ?value2) 
;;		(quantity ?quantity2&:(or (> ?quantity2 ?quantity)(and (= ?quantity2 ?quantity) (< (str-compare ?value2 ?value) 0))))))
;;=>
;;	(modify ?d (calorie-level ?value))
;;)

; ; Rule of tuning "fiber-level"
;;(defrule tuning-fiber-level
;;	(declare (salience 2))
;;	?d <- (dish (ID ?id) (fiber-level ?origin))
;;	(suggestion (dish-id ?id) (attribute "fiber-level") (value ?value&:(neq ?value ?origin)) (quantity ?quantity))
;;	(not (suggestion (dish-id ?id) (attribute "fiber-level") (value ?value2) 
;;		(quantity ?quantity2&:(or (> ?quantity2 ?quantity)(and (= ?quantity2 ?quantity) (< (str-compare ?value2 ?value) 0))))))
;;=>
;;	(modify ?d (fiber-level ?value))
;;)

; ; Rule of tuning "carb-level"
;;(defrule tuning-carb-level
;;	(declare (salience 2))
;;	?d <- (dish (ID ?id) (carb-level ?origin))
;;	(suggestion (dish-id ?id) (attribute "carb-level") (value ?value&:(neq ?value ?origin)) (quantity ?quantity))
;;	(not (suggestion (dish-id ?id) (attribute "carb-level") (value ?value2) 
;;		(quantity ?quantity2&:(or (> ?quantity2 ?quantity)(and (= ?quantity2 ?quantity) (< (str-compare ?value2 ?value) 0))))))
;;=>
;;	(modify ?d (carb-level ?value))
;;)
