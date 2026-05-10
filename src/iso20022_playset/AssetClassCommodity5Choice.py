from . import base_types
from .AssetClassCommodityPolypropylene3Choice import AssetClassCommodityPolypropylene3Choice
from .AssetClassCommodityMultiCommodityExotic1 import AssetClassCommodityMultiCommodityExotic1
from .AssetClassCommodityOther1 import AssetClassCommodityOther1
from .AssetClassCommodityFreight3Choice import AssetClassCommodityFreight3Choice
from .AssetClassCommodityFertilizer3Choice import AssetClassCommodityFertilizer3Choice
from .AssetClassCommodityEnergy2Choice import AssetClassCommodityEnergy2Choice
from .AssetClassCommodityPaper3Choice import AssetClassCommodityPaper3Choice
from .AssetClassCommodityEnvironmental2Choice import AssetClassCommodityEnvironmental2Choice
from .AssetClassCommodityOtherC102Choice import AssetClassCommodityOtherC102Choice
from .AssetClassCommodityInflation1 import AssetClassCommodityInflation1
from .AssetClassCommodityOfficialEconomicStatistics1 import AssetClassCommodityOfficialEconomicStatistics1
from .AssetClassCommodityIndustrialProduct1Choice import AssetClassCommodityIndustrialProduct1Choice
from .AssetClassCommodityMetal1Choice import AssetClassCommodityMetal1Choice
from .AssetClassCommodityAgricultural5Choice import AssetClassCommodityAgricultural5Choice

class AssetClassCommodity5Choice(base_types._BaseFieldType):

	__slots__ = ["_Plprpln", "_OffclEcnmcSttstcs", "_Envttl", "_Frght", "_Frtlzr", "_IndstrlPdct", "_Ppr", "_Metl", "_OthrC10", "_Agrcltrl", "_Othr", "_Nrgy", "_Infltn", "_MultiCmmdtyExtc"]
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
	def MultiCmmdtyExtc(self):
		return self._MultiCmmdtyExtc

	@MultiCmmdtyExtc.setter
	def MultiCmmdtyExtc(self, value):
		self._MultiCmmdtyExtc = value if type(value) != auto else self.make_default("MultiCmmdtyExtc")

	@MultiCmmdtyExtc.deleter
	def MultiCmmdtyExtc(self):
		del self._MultiCmmdtyExtc
		self._MultiCmmdtyExtc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Plprpln', type=AssetClassCommodityPolypropylene3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OffclEcnmcSttstcs', type=AssetClassCommodityOfficialEconomicStatistics1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Envttl', type=AssetClassCommodityEnvironmental2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Frght', type=AssetClassCommodityFreight3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Frtlzr', type=AssetClassCommodityFertilizer3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndstrlPdct', type=AssetClassCommodityIndustrialProduct1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ppr', type=AssetClassCommodityPaper3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Metl', type=AssetClassCommodityMetal1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrC10', type=AssetClassCommodityOtherC102Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Agrcltrl', type=AssetClassCommodityAgricultural5Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=AssetClassCommodityOther1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nrgy', type=AssetClassCommodityEnergy2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Infltn', type=AssetClassCommodityInflation1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MultiCmmdtyExtc', type=AssetClassCommodityMultiCommodityExotic1, min=0, max=1, mutex_group=1, array=False),
	))

