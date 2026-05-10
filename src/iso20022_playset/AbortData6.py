import base_types
import Max35Text
import TrueFalseIndicator
import Max140Text
import ActionMessage11

class AbortData6(base_types._BaseFieldType):

	__slots__ = ["_XchgId", "_AbrtRsn", "_DispOutpt", "_TxSucss"]
	@property
	def XchgId(self):
		return self._XchgId

	@XchgId.setter
	def XchgId(self, value):
		self._XchgId = value if type(value) != auto else self.make_default("XchgId")

	@XchgId.deleter
	def XchgId(self):
		del self._XchgId
		self._XchgId = None

	@property
	def AbrtRsn(self):
		return self._AbrtRsn

	@AbrtRsn.setter
	def AbrtRsn(self, value):
		self._AbrtRsn = value if type(value) != auto else self.make_default("AbrtRsn")

	@AbrtRsn.deleter
	def AbrtRsn(self):
		del self._AbrtRsn
		self._AbrtRsn = None

	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if type(value) != auto else self.make_default("DispOutpt")

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = None

	@property
	def TxSucss(self):
		return self._TxSucss

	@TxSucss.setter
	def TxSucss(self, value):
		self._TxSucss = value if type(value) != auto else self.make_default("TxSucss")

	@TxSucss.deleter
	def TxSucss(self):
		del self._TxSucss
		self._TxSucss = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XchgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AbrtRsn', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSucss', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

