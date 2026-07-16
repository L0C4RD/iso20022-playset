# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PaperCommodityContainerBoard2
from . import PaperCommodityNewsprint2
from . import PaperCommodityOther1
from . import PaperCommodityPulp2

class AssetClassCommodityPaper4Choice(base_types._BaseFieldType):

	__slots__ = ["_CntnrBrd", "_Nwsprnt", "_Othr", "_Pulp", "_RcvrdPpr"]
	@property
	def CntnrBrd(self):
		return self._CntnrBrd

	@CntnrBrd.setter
	def CntnrBrd(self, value):
		self._CntnrBrd = value if value is not None else base_types.UninitialisedField(self, 'CntnrBrd', PaperCommodityContainerBoard2, False)

	@CntnrBrd.deleter
	def CntnrBrd(self):
		del self._CntnrBrd
		self._CntnrBrd = base_types.UninitialisedField(self, 'CntnrBrd', PaperCommodityContainerBoard2, False)

	@property
	def Nwsprnt(self):
		return self._Nwsprnt

	@Nwsprnt.setter
	def Nwsprnt(self, value):
		self._Nwsprnt = value if value is not None else base_types.UninitialisedField(self, 'Nwsprnt', PaperCommodityNewsprint2, False)

	@Nwsprnt.deleter
	def Nwsprnt(self):
		del self._Nwsprnt
		self._Nwsprnt = base_types.UninitialisedField(self, 'Nwsprnt', PaperCommodityNewsprint2, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', PaperCommodityOther1, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', PaperCommodityOther1, False)

	@property
	def Pulp(self):
		return self._Pulp

	@Pulp.setter
	def Pulp(self, value):
		self._Pulp = value if value is not None else base_types.UninitialisedField(self, 'Pulp', PaperCommodityPulp2, False)

	@Pulp.deleter
	def Pulp(self):
		del self._Pulp
		self._Pulp = base_types.UninitialisedField(self, 'Pulp', PaperCommodityPulp2, False)

	@property
	def RcvrdPpr(self):
		return self._RcvrdPpr

	@RcvrdPpr.setter
	def RcvrdPpr(self, value):
		self._RcvrdPpr = value if value is not None else base_types.UninitialisedField(self, 'RcvrdPpr', PaperCommodityOther1, False)

	@RcvrdPpr.deleter
	def RcvrdPpr(self):
		del self._RcvrdPpr
		self._RcvrdPpr = base_types.UninitialisedField(self, 'RcvrdPpr', PaperCommodityOther1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntnrBrd', type=PaperCommodityContainerBoard2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nwsprnt', type=PaperCommodityNewsprint2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=PaperCommodityOther1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pulp', type=PaperCommodityPulp2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcvrdPpr', type=PaperCommodityOther1, min=0, max=1, mutex_group=1, array=False),
	))