import base_types
import PaperCommodityNewsprint1
import PaperCommodityContainerBoard1
import PaperCommodityPulp1
import PaperCommodityRecoveredPaper2
import PaperCommodityRecoveredPaper1

class AssetClassCommodityPaper3Choice(base_types._BaseFieldType):

	__slots__ = ["_Nwsprnt", "_Pulp", "_CntnrBrd", "_Othr", "_RcvrdPpr"]
	@property
	def Nwsprnt(self):
		return self._Nwsprnt

	@Nwsprnt.setter
	def Nwsprnt(self, value):
		self._Nwsprnt = value if type(value) != auto else self.make_default("Nwsprnt")

	@Nwsprnt.deleter
	def Nwsprnt(self):
		del self._Nwsprnt
		self._Nwsprnt = None

	@property
	def Pulp(self):
		return self._Pulp

	@Pulp.setter
	def Pulp(self, value):
		self._Pulp = value if type(value) != auto else self.make_default("Pulp")

	@Pulp.deleter
	def Pulp(self):
		del self._Pulp
		self._Pulp = None

	@property
	def CntnrBrd(self):
		return self._CntnrBrd

	@CntnrBrd.setter
	def CntnrBrd(self, value):
		self._CntnrBrd = value if type(value) != auto else self.make_default("CntnrBrd")

	@CntnrBrd.deleter
	def CntnrBrd(self):
		del self._CntnrBrd
		self._CntnrBrd = None

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
	def RcvrdPpr(self):
		return self._RcvrdPpr

	@RcvrdPpr.setter
	def RcvrdPpr(self, value):
		self._RcvrdPpr = value if type(value) != auto else self.make_default("RcvrdPpr")

	@RcvrdPpr.deleter
	def RcvrdPpr(self):
		del self._RcvrdPpr
		self._RcvrdPpr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nwsprnt', type=PaperCommodityNewsprint1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pulp', type=PaperCommodityPulp1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CntnrBrd', type=PaperCommodityContainerBoard1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=PaperCommodityRecoveredPaper2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcvrdPpr', type=PaperCommodityRecoveredPaper1, min=0, max=1, mutex_group=1, array=False),
	))

