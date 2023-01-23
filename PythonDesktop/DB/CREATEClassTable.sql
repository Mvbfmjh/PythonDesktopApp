CREATE TABLE IF NOT EXISTS Class (
	CLS INTEGER PRIMARY KEY AUTOINCREMENT, 
	クラス名 TEXT UNIQUE,
	クラス階級 TINYINT,
	クラスレベル TINYINT,
	クラス性別 BLOB,
	クラス移動種 TEXT,
	有効 TEXT,

	HP_成長 TINYINT,
	力_成長 TINYINT,
	魔力_成長 TINYINT,
	技_成長 TINYINT,
	速さ_成長 TINYINT,
	幸運_成長 TINYINT,
	守備_成長 TINYINT,
	魔防_成長 TINYINT,
	魅力_成長 TINYINT,

	HP_基礎 TINYINT,
	力_基礎 TINYINT,
	魔力_基礎 TINYINT,
	技_基礎 TINYINT,
	速さ_基礎 TINYINT,
	幸運_基礎 TINYINT,
	守備_基礎 TINYINT,
	魔防_基礎 TINYINT,
	魅力_基礎 TINYINT,

	技能_剣術 TINYINT,
	技能_槍術 TINYINT,
	技能_斧術 TINYINT,
	技能_弓術 TINYINT,
	技能_格闘術 TINYINT,
	技能_理学 TINYINT,
	技能_信仰 TINYINT,
	技能_指揮 TINYINT,
	技能_重装 TINYINT,
	技能_馬術 TINYINT,
	技能_飛行 TINYINT
	)