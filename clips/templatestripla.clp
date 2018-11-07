; ; Templates
; ; Template to represent "dish".
(deftemplate enfermedad
  (slot ID (type NUMBER))
  (slot name (type STRING))
  (slot planta (type STRING))
  (slot sintoma-aa (type STRING))
  (slot sintoma-bb (type STRING))
;;  (slot calorie-level (type STRING))
;;  (slot fiber-level (type STRING))
;;  (slot fat-level (type STRING))
;;  (slot carb-level (type STRING))
  (slot sintoma-dd (type STRING))
;;  (slot sour-level (type STRING))
  (slot sintoma-ee (type STRING))
  (slot sintoma-cc (type STRING))
  (slot stars (type NUMBER))
)

; ; Template to represent user's preference.
(deftemplate preference
  (slot planta (type STRING))
  (slot sintoma-aa (type STRING))
  (slot sintoma-bb (type STRING))
;;  (slot calorie-level (type STRING))
;;  (slot fiber-level (type STRING))
;;  (slot fat-level (type STRING))
;;  (slot carb-level (type STRING))
  (slot sintoma-dd (type STRING))
;;  (slot sour-level (type STRING))
  (slot sintoma-ee (type STRING))
  (slot sintoma-cc (type STRING))
)

; ; Template to represent user's reviews.
(deftemplate review
  (slot ID (type NUMBER))
  (slot stars (type NUMBER))
  (slot enfermedad-name (type STRING))
  (slot enfermedad-id (type NUMBER))
  (slot reviewer (type STRING))
  (slot comment (type STRING))
)


; ; Template to represent user's suggestions (for fine-tuning dishes).
(deftemplate suggestion
  (slot enfermedad-name (type STRING))
  (slot enfermedad-id (type NUMBER))
  (slot attribute (type STRING))
  (slot value (type STRING))
  (slot quantity (type NUMBER))
)
