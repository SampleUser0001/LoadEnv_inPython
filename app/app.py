# -*- coding: utf-8 -*-
import settings

keyIndex = 0
tmp1 = settings.ENV_DIC[settings.ENV_KEYS[keyIndex]]
keyIndex = keyIndex + 1

tmp2 = settings.ENV_DIC[settings.ENV_KEYS[keyIndex]]
keyIndex = keyIndex + 1

tmp3 = settings.ENV_DIC[settings.ENV_KEYS[keyIndex]]
keyIndex = keyIndex + 1

if __name__ == '__main__':
  print(settings.ENV_DIC)
  print(tmp1)
  print(tmp2)
  print(tmp3)
