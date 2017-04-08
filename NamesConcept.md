## Conception for App model architecture

#### XX.YY.Z.NN[.RR]

.RR - optional

#### Name ID keys general description:

| Key     | Description     |
| :------------- | :------------- |
| **XX** | Area: Myth, Regular names, Ancient names, etc  |
| **YY** | Category of Area. Greek Myth, Roman Myth, etc  |
| **Z** | Gender: 0 - Masculine, 1 - Feminine  |
| **NN** | Index number of name in plist file  |
| **RR** | Race in selected category (if applicable)  |

For example:
> 01.02.0.15 = Myth, Vedic, Masculine, 15th name in Plist

> 02.02.1.2.03 = Fiction, Tolkien, Feminine, 2nd name in Plist, Hobbits race

#### Specific ID keys description:
##### Area
| Area Key     | Description     |
| :------------- | :------------- |
| **01** | Mythological  |
| **02** | Fiction and Fantasy  |
| **03** | Ancient names  |

##### Category of Area
| Area Key     | Category Key     | Description |
| :------------- | :------------- | ------ |
| **01** | **01** | Mythological |
| | **02** | Vedic |
| | **03** | Roman |
| | **04** | Norse |
| | **05** | Egypt |
| | **06** | Persian |
| | **07** | Celtic |
| **02** | **01** | Dune |
| | **02** | Tolkien |

##### Races of categories
| Area Key     | Category Key     | Race Key | Description |
| :------------- | :------------- | ------ | ----- |
| **02** | **02** | 01 | Elves |
|  |  | 02 | Men |
|  |  | 03 | Hobbits |
|  |  | 04 | Dwarves |
|  |  | 05 | Ainur |
|  |  | 06 | Orcs |
|  |  | 07 | Ents |
|  |  | 08 | Dragons |
