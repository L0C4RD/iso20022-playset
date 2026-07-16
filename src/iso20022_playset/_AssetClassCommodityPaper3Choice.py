# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PaperCommodityContainerBoard1
from . import PaperCommodityNewsprint1
from . import PaperCommodityPulp1
from . import PaperCommodityRecoveredPaper1
from . import PaperCommodityRecoveredPaper2

class AssetClassCommodityPaper3Choice(base_types._BaseFieldType):

	__slots__ = ["_CntnrBrd", "_Nwsprnt", "_Othr", "_Pulp", "_RcvrdPpr"]
	@property
	def CntnrBrd(self):
		return self._CntnrBrd

	@CntnrBrd.setter
	def CntnrBrd(self, value):
		self._CntnrBrd = value if value is not None else base_types.UninitialisedField(self, 'CntnrBrd', PaperCommodityContainerBoard1, False)

	@CntnrBrd.deleter
	def CntnrBrd(self):
		del self._CntnrBrd
		self._CntnrBrd = base_types.UninitialisedField(self, 'CntnrBrd', PaperCommodityContainerBoard1, False)

	@property
	def Nwsprnt(self):
		return self._Nwsprnt

	@Nwsprnt.setter
	def Nwsprnt(self, value):
		self._Nwsprnt = value if value is not None else base_types.UninitialisedField(self, 'Nwsprnt', PaperCommodityNewsprint1, False)

	@Nwsprnt.deleter
	def Nwsprnt(self):
		del self._Nwsprnt
		self._Nwsprnt = base_types.UninitialisedField(self, 'Nwsprnt', PaperCommodityNewsprint1, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', PaperCommodityRecoveredPaper2, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', PaperCommodityRecoveredPaper2, False)

	@property
	def Pulp(self):
		return self._Pulp

	@Pulp.setter
	def Pulp(self, value):
		self._Pulp = value if value is not None else base_types.UninitialisedField(self, 'Pulp', PaperCommodityPulp1, False)

	@Pulp.deleter
	def Pulp(self):
		del self._Pulp
		self._Pulp = base_types.UninitialisedField(self, 'Pulp', PaperCommodityPulp1, False)

	@property
	def RcvrdPpr(self):
		return self._RcvrdPpr

	@RcvrdPpr.setter
	def RcvrdPpr(self, value):
		self._RcvrdPpr = value if value is not None else base_types.UninitialisedField(self, 'RcvrdPpr', PaperCommodityRecoveredPaper1, False)

	@RcvrdPpr.deleter
	def RcvrdPpr(self):
		del self._RcvrdPpr
		self._RcvrdPpr = base_types.UninitialisedField(self, 'RcvrdPpr', PaperCommodityRecoveredPaper1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntnrBrd', type=PaperCommodityContainerBoard1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nwsprnt', type=PaperCommodityNewsprint1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=PaperCommodityRecoveredPaper2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pulp', type=PaperCommodityPulp1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcvrdPpr', type=PaperCommodityRecoveredPaper1, min=0, max=1, mutex_group=1, array=False),
	))