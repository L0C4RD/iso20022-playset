# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AssetClassCommodityAgricultural1Choice
from . import AssetClassCommodityEnergy1Choice
from . import AssetClassCommodityEnvironmental1Choice
from . import AssetClassCommodityFertilizer1Choice
from . import AssetClassCommodityFreight1Choice
from . import AssetClassCommodityIndustrialProduct1Choice
from . import AssetClassCommodityInflation1
from . import AssetClassCommodityMetal1Choice
from . import AssetClassCommodityMultiCommodityExotic1
from . import AssetClassCommodityOfficialEconomicStatistics1
from . import AssetClassCommodityOther1
from . import AssetClassCommodityOtherC102Choice
from . import AssetClassCommodityPaper1Choice
from . import AssetClassCommodityPolypropylene1Choice

class AssetClassCommodity3Choice(base_types._BaseFieldType):

	__slots__ = ["_Agrcltrl", "_Envttl", "_Frght", "_Frtlzr", "_IndstrlPdct", "_Infltn", "_Metl", "_MultiCmmdtyExtc", "_Nrgy", "_OffclEcnmcSttstcs", "_Othr", "_OthrC10", "_Plprpln", "_Ppr"]
	@property
	def Agrcltrl(self):
		return self._Agrcltrl

	@Agrcltrl.setter
	def Agrcltrl(self, value):
		self._Agrcltrl = value if value is not None else base_types.UninitialisedField(self, 'Agrcltrl', AssetClassCommodityAgricultural1Choice, False)

	@Agrcltrl.deleter
	def Agrcltrl(self):
		del self._Agrcltrl
		self._Agrcltrl = base_types.UninitialisedField(self, 'Agrcltrl', AssetClassCommodityAgricultural1Choice, False)

	@property
	def Envttl(self):
		return self._Envttl

	@Envttl.setter
	def Envttl(self, value):
		self._Envttl = value if value is not None else base_types.UninitialisedField(self, 'Envttl', AssetClassCommodityEnvironmental1Choice, False)

	@Envttl.deleter
	def Envttl(self):
		del self._Envttl
		self._Envttl = base_types.UninitialisedField(self, 'Envttl', AssetClassCommodityEnvironmental1Choice, False)

	@property
	def Frght(self):
		return self._Frght

	@Frght.setter
	def Frght(self, value):
		self._Frght = value if value is not None else base_types.UninitialisedField(self, 'Frght', AssetClassCommodityFreight1Choice, False)

	@Frght.deleter
	def Frght(self):
		del self._Frght
		self._Frght = base_types.UninitialisedField(self, 'Frght', AssetClassCommodityFreight1Choice, False)

	@property
	def Frtlzr(self):
		return self._Frtlzr

	@Frtlzr.setter
	def Frtlzr(self, value):
		self._Frtlzr = value if value is not None else base_types.UninitialisedField(self, 'Frtlzr', AssetClassCommodityFertilizer1Choice, False)

	@Frtlzr.deleter
	def Frtlzr(self):
		del self._Frtlzr
		self._Frtlzr = base_types.UninitialisedField(self, 'Frtlzr', AssetClassCommodityFertilizer1Choice, False)

	@property
	def IndstrlPdct(self):
		return self._IndstrlPdct

	@IndstrlPdct.setter
	def IndstrlPdct(self, value):
		self._IndstrlPdct = value if value is not None else base_types.UninitialisedField(self, 'IndstrlPdct', AssetClassCommodityIndustrialProduct1Choice, False)

	@IndstrlPdct.deleter
	def IndstrlPdct(self):
		del self._IndstrlPdct
		self._IndstrlPdct = base_types.UninitialisedField(self, 'IndstrlPdct', AssetClassCommodityIndustrialProduct1Choice, False)

	@property
	def Infltn(self):
		return self._Infltn

	@Infltn.setter
	def Infltn(self, value):
		self._Infltn = value if value is not None else base_types.UninitialisedField(self, 'Infltn', AssetClassCommodityInflation1, False)

	@Infltn.deleter
	def Infltn(self):
		del self._Infltn
		self._Infltn = base_types.UninitialisedField(self, 'Infltn', AssetClassCommodityInflation1, False)

	@property
	def Metl(self):
		return self._Metl

	@Metl.setter
	def Metl(self, value):
		self._Metl = value if value is not None else base_types.UninitialisedField(self, 'Metl', AssetClassCommodityMetal1Choice, False)

	@Metl.deleter
	def Metl(self):
		del self._Metl
		self._Metl = base_types.UninitialisedField(self, 'Metl', AssetClassCommodityMetal1Choice, False)

	@property
	def MultiCmmdtyExtc(self):
		return self._MultiCmmdtyExtc

	@MultiCmmdtyExtc.setter
	def MultiCmmdtyExtc(self, value):
		self._MultiCmmdtyExtc = value if value is not None else base_types.UninitialisedField(self, 'MultiCmmdtyExtc', AssetClassCommodityMultiCommodityExotic1, False)

	@MultiCmmdtyExtc.deleter
	def MultiCmmdtyExtc(self):
		del self._MultiCmmdtyExtc
		self._MultiCmmdtyExtc = base_types.UninitialisedField(self, 'MultiCmmdtyExtc', AssetClassCommodityMultiCommodityExotic1, False)

	@property
	def Nrgy(self):
		return self._Nrgy

	@Nrgy.setter
	def Nrgy(self, value):
		self._Nrgy = value if value is not None else base_types.UninitialisedField(self, 'Nrgy', AssetClassCommodityEnergy1Choice, False)

	@Nrgy.deleter
	def Nrgy(self):
		del self._Nrgy
		self._Nrgy = base_types.UninitialisedField(self, 'Nrgy', AssetClassCommodityEnergy1Choice, False)

	@property
	def OffclEcnmcSttstcs(self):
		return self._OffclEcnmcSttstcs

	@OffclEcnmcSttstcs.setter
	def OffclEcnmcSttstcs(self, value):
		self._OffclEcnmcSttstcs = value if value is not None else base_types.UninitialisedField(self, 'OffclEcnmcSttstcs', AssetClassCommodityOfficialEconomicStatistics1, False)

	@OffclEcnmcSttstcs.deleter
	def OffclEcnmcSttstcs(self):
		del self._OffclEcnmcSttstcs
		self._OffclEcnmcSttstcs = base_types.UninitialisedField(self, 'OffclEcnmcSttstcs', AssetClassCommodityOfficialEconomicStatistics1, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', AssetClassCommodityOther1, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', AssetClassCommodityOther1, False)

	@property
	def OthrC10(self):
		return self._OthrC10

	@OthrC10.setter
	def OthrC10(self, value):
		self._OthrC10 = value if value is not None else base_types.UninitialisedField(self, 'OthrC10', AssetClassCommodityOtherC102Choice, False)

	@OthrC10.deleter
	def OthrC10(self):
		del self._OthrC10
		self._OthrC10 = base_types.UninitialisedField(self, 'OthrC10', AssetClassCommodityOtherC102Choice, False)

	@property
	def Plprpln(self):
		return self._Plprpln

	@Plprpln.setter
	def Plprpln(self, value):
		self._Plprpln = value if value is not None else base_types.UninitialisedField(self, 'Plprpln', AssetClassCommodityPolypropylene1Choice, False)

	@Plprpln.deleter
	def Plprpln(self):
		del self._Plprpln
		self._Plprpln = base_types.UninitialisedField(self, 'Plprpln', AssetClassCommodityPolypropylene1Choice, False)

	@property
	def Ppr(self):
		return self._Ppr

	@Ppr.setter
	def Ppr(self, value):
		self._Ppr = value if value is not None else base_types.UninitialisedField(self, 'Ppr', AssetClassCommodityPaper1Choice, False)

	@Ppr.deleter
	def Ppr(self):
		del self._Ppr
		self._Ppr = base_types.UninitialisedField(self, 'Ppr', AssetClassCommodityPaper1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Agrcltrl', type=AssetClassCommodityAgricultural1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Envttl', type=AssetClassCommodityEnvironmental1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Frght', type=AssetClassCommodityFreight1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Frtlzr', type=AssetClassCommodityFertilizer1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndstrlPdct', type=AssetClassCommodityIndustrialProduct1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Infltn', type=AssetClassCommodityInflation1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Metl', type=AssetClassCommodityMetal1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MultiCmmdtyExtc', type=AssetClassCommodityMultiCommodityExotic1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nrgy', type=AssetClassCommodityEnergy1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OffclEcnmcSttstcs', type=AssetClassCommodityOfficialEconomicStatistics1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=AssetClassCommodityOther1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrC10', type=AssetClassCommodityOtherC102Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Plprpln', type=AssetClassCommodityPolypropylene1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ppr', type=AssetClassCommodityPaper1Choice, min=0, max=1, mutex_group=1, array=False),
	))