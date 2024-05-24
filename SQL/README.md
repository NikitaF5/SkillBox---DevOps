# Мои решения заданий с курсов

## Запрос 1
Получение списка id и имён товаров, количество которых на складе более 518 штук
```sql
SELECT `id`, `name`
FROM `good`
WHERE `count` > 518;
```

## Запрос 2
Получение списка id, имён и цен закончившихся товаров, цена которых не менее 300 рублей
```sql
SELECT `id`, `name`, `price`
FROM `good`
WHERE `count` = 0 AND `price` >= 300;
```

## Запрос 3
Получение списка id и имён товаров, в названии которых встречается слово «таёжный»
```sql
SELECT `id`, `name`
FROM `good`
WHERE `name` LIKE '%таёжный%';
```

## Запрос 4
Получение списка id, имён и дат регистрации пользователей с именем Иван, зарегистрировавшихся весной, летом или осенью 2017-го года
```sql
SELECT `id`, `name`, `registration_date`
FROM `user`
WHERE `name` = 'Иван'
  AND YEAR(`reg_date`) = 2017
  AND MONTH(`reg_date`) IN (3, 4, 5, 6, 7, 8, 9, 10, 11);
```

## Запрос 5
Получение списка id и имён товаров, в названии которых встречается слово «манго», но не встречается слово «айс»
```sql
SELECT `id`, `name`
FROM `good`
WHERE `name` LIKE '%манго%' AND `name` NOT LIKE '%айс%';
```

## Запрос 6
Получение списка пяти id и имён товаров, которых больше всего на складе, а также их количества
```sql
SELECT `id`, `name`, `count`
FROM `good`
ORDER BY `count` DESC
LIMIT 5;
```

## Запрос 7
Получение списка email-ов десяти последних зарегистрировавшихся пользователей
```sql
SELECT `email`
FROM `user`
ORDER BY `reg_date` DESC
LIMIT 10;
```

## Запрос 8
Вывести id статусов заказов, которые вообще встречаются в таблице order
```sql
SELECT DISTINCT `status_id`
FROM `order`;
```

## Запрос 9
Вывести id товаров и количества заказов, в которых они встречаются
```sql
SELECT `g`.`id`, COUNT(`o2g`.`order_id`) as `count`
FROM `good` `g`
JOIN `order2good` `o2g` ON `g`.`id` = `o2g`.`good_id`
GROUP BY `g`.`id`;
```

## Запрос 10
Вывести имена статусов заказов и количества заказов, находящихся в этих статусах
```sql
SELECT `os`.`name`, COUNT(`o`.`id`) as `count`
FROM `order` `o`
JOIN `order_status` `os` ON `o`.`status_id` = `os`.`id`
GROUP BY `os`.`name`;
```

## Запрос 11
Вывести имена пользователей, заказавших хотя бы раз «пуэр с молоком»
```sql
SELECT DISTINCT `u`.`name`
FROM `user` `u`
JOIN `order` `o` ON `u`.`id` = `o`.`user_id`
JOIN `order2good` `o2g` ON `o`.`id` = `o2g`.`order_id`
JOIN `good` `g` ON `o2g`.`good_id` = `g`.`id`
WHERE `g`.`name` = 'пуэр с молоком';
```

## Запрос 12
Вывести id и названия товаров, которые никогда не заказывались
```sql
SELECT `id`, `name`
FROM `good`
WHERE `id` NOT IN (
    SELECT `good_id`
    FROM `order2good`
);
```

## Запрос 13
Добавьте при помощи INSERT-запросов четыре новых товара в таблицу good с ценами выше 1000 рублей и ненулевым количеством
```sql
INSERT INTO `good` (`name`, `price`, `count`) VALUES
('Товар 1', 1500, 10),
('Товар 2', 2000, 20),
('Товар 3', 2500, 30),
('Товар 4', 3000, 40);
```

## Запрос 14
Обнулите количество товаров, цена которых выше 1000 рублей, используя один UPDATE-запрос
```sql
UPDATE `good`
SET `count` = 0
WHERE `price` > 1000;
```

## Запрос 15
Повысьте цену у всех товаров, которые дороже 1000 рублей, в три раза, используя один UPDATE-запрос
```sql
UPDATE `good`
SET `price` = `price` * 3
WHERE `price` > 1000;
```

## Запрос 16
Удалите добавленные вами товары, используя один DELETE-запрос и условие «дороже 1000 рублей»
```sql
DELETE FROM `good`
WHERE `price` > 1000 AND `name` IN ('Товар 1', 'Товар 2', 'Товар 3', 'Товар 4');
```

## Запрос 17
Получение информации о заказах с пометкой о просрочке
```sql
SELECT `o`.`id`, `o`.`status_id`, `o`.`creation_date`,
       CASE
           WHEN `o`.`status_id` IN (7, 8) THEN
               CASE
                   WHEN `o`.`creation_date` < DATE_SUB(NOW(), INTERVAL 1 YEAR) THEN 'Старый'
                   ELSE 'Новый'
               END
           ELSE
               CASE
                   WHEN `o`.`creation_date` < DATE_SUB(NOW(), INTERVAL 1 YEAR) THEN 'Устаревший'
                   ELSE 'Новый'
               END
       END AS `label`
FROM `order` `o`
ORDER BY `o`.`status_id` ASC, `o`.`creation_date` DESC;
```

## Запрос 18
Получение пользователей с пометкой о лояльности
```sql
SELECT `u`.`id`, `u`.`name`,
       CASE
           WHEN `u`.`reg_date` < DATE_SUB('2022-03-17', INTERVAL 5 YEAR) OR (
               SELECT COUNT(*) FROM `order` `o` WHERE `o`.`user_id` = `u`.`id`) > 1 THEN 'Лояльный'
           ELSE 'Новый'
       END AS `loyalty_label`
FROM `user` `u`;
```



