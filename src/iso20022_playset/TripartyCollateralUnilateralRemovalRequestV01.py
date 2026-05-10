import base_types
import Max35Text
import CollateralRole1Code
import Pagination1
import SupplementaryData1
import PartyIdentification232
import RequestDetails28

class TripartyCollateralUnilateralRemovalRequestV01(base_types._BaseFieldType):

	__slots__ = ["_RmvlReqId", "_SplmtryData", "_Pgntn", "_CollSd", "_ReqDtls", "_ClntPtyA", "_PtyA"]
	@property
	def RmvlReqId(self):
		return self._RmvlReqId

	@RmvlReqId.setter
	def RmvlReqId(self, value):
		self._RmvlReqId = value if type(value) != auto else self.make_default("RmvlReqId")

	@RmvlReqId.deleter
	def RmvlReqId(self):
		del self._RmvlReqId
		self._RmvlReqId = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def CollSd(self):
		return self._CollSd

	@CollSd.setter
	def CollSd(self, value):
		self._CollSd = value if type(value) != auto else self.make_default("CollSd")

	@CollSd.deleter
	def CollSd(self):
		del self._CollSd
		self._CollSd = None

	@property
	def ReqDtls(self):
		return self._ReqDtls

	@ReqDtls.setter
	def ReqDtls(self, value):
		self._ReqDtls = value if type(value) != auto else self.make_default("ReqDtls")

	@ReqDtls.deleter
	def ReqDtls(self):
		del self._ReqDtls
		self._ReqDtls = None

	@property
	def ClntPtyA(self):
		return self._ClntPtyA

	@ClntPtyA.setter
	def ClntPtyA(self, value):
		self._ClntPtyA = value if type(value) != auto else self.make_default("ClntPtyA")

	@ClntPtyA.deleter
	def ClntPtyA(self):
		del self._ClntPtyA
		self._ClntPtyA = None

	@property
	def PtyA(self):
		return self._PtyA

	@PtyA.setter
	def PtyA(self, value):
		self._PtyA = value if type(value) != auto else self.make_default("PtyA")

	@PtyA.deleter
	def PtyA(self):
		del self._PtyA
		self._PtyA = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RmvlReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSd', type=CollateralRole1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqDtls', type=RequestDetails28, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntPtyA', type=PartyIdentification232, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyA', type=PartyIdentification232, min=1, max=1, mutex_group=None, array=False),
	))

