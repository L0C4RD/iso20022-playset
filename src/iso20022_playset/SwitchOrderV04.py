import base_types
import Pagination
import Extension1
import AdditionalReference9
import AdditionalReference8
import MessageIdentification1
import CopyInformation4
import SwitchOrder7

class SwitchOrderV04(base_types._BaseFieldType):

	__slots__ = ["_MsgPgntn", "_CpyDtls", "_SwtchOrdrDtls", "_PrvsRef", "_PoolRef", "_Xtnsn", "_MsgId"]
	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if type(value) != auto else self.make_default("MsgPgntn")

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = None

	@property
	def CpyDtls(self):
		return self._CpyDtls

	@CpyDtls.setter
	def CpyDtls(self, value):
		self._CpyDtls = value if type(value) != auto else self.make_default("CpyDtls")

	@CpyDtls.deleter
	def CpyDtls(self):
		del self._CpyDtls
		self._CpyDtls = None

	@property
	def SwtchOrdrDtls(self):
		return self._SwtchOrdrDtls

	@SwtchOrdrDtls.setter
	def SwtchOrdrDtls(self, value):
		self._SwtchOrdrDtls = value if type(value) != auto else self.make_default("SwtchOrdrDtls")

	@SwtchOrdrDtls.deleter
	def SwtchOrdrDtls(self):
		del self._SwtchOrdrDtls
		self._SwtchOrdrDtls = None

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if type(value) != auto else self.make_default("PrvsRef")

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = None

	@property
	def PoolRef(self):
		return self._PoolRef

	@PoolRef.setter
	def PoolRef(self, value):
		self._PoolRef = value if type(value) != auto else self.make_default("PoolRef")

	@PoolRef.deleter
	def PoolRef(self):
		del self._PoolRef
		self._PoolRef = None

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if type(value) != auto else self.make_default("Xtnsn")

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgPgntn', type=Pagination, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpyDtls', type=CopyInformation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwtchOrdrDtls', type=SwitchOrder7, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

