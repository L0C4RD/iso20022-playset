import base_types
import AssetClassCommodityEnergy1Choice
import AssetClassCommodityInflation1
import AssetClassCommodityPaper1Choice
import AssetClassCommodityOfficialEconomicStatistics1
import AssetClassCommodityOtherC102Choice
import AssetClassCommodityFertilizer1Choice
import AssetClassCommodityMetal1Choice
import AssetClassCommodityIndustrialProduct1Choice
import AssetClassCommodityEnvironmental1Choice
import AssetClassCommodityPolypropylene1Choice
import AssetClassCommodityFreight1Choice
import AssetClassCommodityMultiCommodityExotic1
import AssetClassCommodityAgricultural1Choice
import AssetClassCommodityOther1

class AssetClassCommodity3Choice(base_types._BaseFieldType):

	__slots__ = ["_Frtlzr", "_OthrC10", "_Nrgy", "_Metl", "_Frght", "_IndstrlPdct", "_MultiCmmdtyExtc", "_Othr", "_OffclEcnmcSttstcs", "_Agrcltrl", "_Infltn", "_Envttl", "_Ppr", "_Plprpln"]
	@property
	def Frtlzr(self):
		return self._Frtlzr

	@Frtlzr.setter
	def Frtlzr(self, value):
		self._Frtlzr = value if type(value) != auto else self.make_default("Frtlzr")

	@Frtlzr.deleter
	def Frtlzr(self):
		del self._Frtlzr
		self._Frtlzr = None

	@property
	def OthrC10(self):
		return self._OthrC10

	@OthrC10.setter
	def OthrC10(self, value):
		self._OthrC10 = value if type(value) != auto else self.make_default("OthrC10")

	@OthrC10.deleter
	def OthrC10(self):
		del self._OthrC10
		self._OthrC10 = None

	@property
	def Nrgy(self):
		return self._Nrgy

	@Nrgy.setter
	def Nrgy(self, value):
		self._Nrgy = value if type(value) != auto else self.make_default("Nrgy")

	@Nrgy.deleter
	def Nrgy(self):
		del self._Nrgy
		self._Nrgy = None

	@property
	def Metl(self):
		return self._Metl

	@Metl.setter
	def Metl(self, value):
		self._Metl = value if type(value) != auto else self.make_default("Metl")

	@Metl.deleter
	def Metl(self):
		del self._Metl
		self._Metl = None

	@property
	def Frght(self):
		return self._Frght

	@Frght.setter
	def Frght(self, value):
		self._Frght = value if type(value) != auto else self.make_default("Frght")

	@Frght.deleter
	def Frght(self):
		del self._Frght
		self._Frght = None

	@property
	def IndstrlPdct(self):
		return self._IndstrlPdct

	@IndstrlPdct.setter
	def IndstrlPdct(self, value):
		self._IndstrlPdct = value if type(value) != auto else self.make_default("IndstrlPdct")

	@IndstrlPdct.deleter
	def IndstrlPdct(self):
		del self._IndstrlPdct
		self._IndstrlPdct = None

	@property
	def MultiCmmdtyExtc(self):
		return self._MultiCmmdtyExtc

	@MultiCmmdtyExtc.setter
	def MultiCmmdtyExtc(self, value):
		self._MultiCmmdtyExtc = value if type(value) != auto else self.make_default("MultiCmmdtyExtc")

	@MultiCmmdtyExtc.deleter
	def MultiCmmdtyExtc(self):
		del self._MultiCmmdtyExtc
		self._MultiCmmdtyExtc = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def OffclEcnmcSttstcs(self):
		return self._OffclEcnmcSttstcs

	@OffclEcnmcSttstcs.setter
	def OffclEcnmcSttstcs(self, value):
		self._OffclEcnmcSttstcs = value if type(value) != auto else self.make_default("OffclEcnmcSttstcs")

	@OffclEcnmcSttstcs.deleter
	def OffclEcnmcSttstcs(self):
		del self._OffclEcnmcSttstcs
		self._OffclEcnmcSttstcs = None

	@property
	def Agrcltrl(self):
		return self._Agrcltrl

	@Agrcltrl.setter
	def Agrcltrl(self, value):
		self._Agrcltrl = value if type(value) != auto else self.make_default("Agrcltrl")

	@Agrcltrl.deleter
	def Agrcltrl(self):
		del self._Agrcltrl
		self._Agrcltrl = None

	@property
	def Infltn(self):
		return self._Infltn

	@Infltn.setter
	def Infltn(self, value):
		self._Infltn = value if type(value) != auto else self.make_default("Infltn")

	@Infltn.deleter
	def Infltn(self):
		del self._Infltn
		self._Infltn = None

	@property
	def Envttl(self):
		return self._Envttl

	@Envttl.setter
	def Envttl(self, value):
		self._Envttl = value if type(value) != auto else self.make_default("Envttl")

	@Envttl.deleter
	def Envttl(self):
		del self._Envttl
		self._Envttl = None

	@property
	def Ppr(self):
		return self._Ppr

	@Ppr.setter
	def Ppr(self, value):
		self._Ppr = value if type(value) != auto else self.make_default("Ppr")

	@Ppr.deleter
	def Ppr(self):
		del self._Ppr
		self._Ppr = None

	@property
	def Plprpln(self):
		return self._Plprpln

	@Plprpln.setter
	def Plprpln(self, value):
		self._Plprpln = value if type(value) != auto else self.make_default("Plprpln")

	@Plprpln.deleter
	def Plprpln(self):
		del self._Plprpln
		self._Plprpln = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frtlzr', type=AssetClassCommodityFertilizer1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrC10', type=AssetClassCommodityOtherC102Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nrgy', type=AssetClassCommodityEnergy1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Metl', type=AssetClassCommodityMetal1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Frght', type=AssetClassCommodityFreight1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndstrlPdct', type=AssetClassCommodityIndustrialProduct1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MultiCmmdtyExtc', type=AssetClassCommodityMultiCommodityExotic1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=AssetClassCommodityOther1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OffclEcnmcSttstcs', type=AssetClassCommodityOfficialEconomicStatistics1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Agrcltrl', type=AssetClassCommodityAgricultural1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Infltn', type=AssetClassCommodityInflation1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Envttl', type=AssetClassCommodityEnvironmental1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ppr', type=AssetClassCommodityPaper1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Plprpln', type=AssetClassCommodityPolypropylene1Choice, min=0, max=1, mutex_group=1, array=False),
	))

