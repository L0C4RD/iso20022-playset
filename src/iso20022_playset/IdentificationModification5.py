import base_types
import Max35Text
import IdentificationInformation5
import Max140Text

class IdentificationModification5(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Id", "_OrgnlPtyAndAcctId", "_UpdtdPtyAndAcctId"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def OrgnlPtyAndAcctId(self):
		return self._OrgnlPtyAndAcctId

	@OrgnlPtyAndAcctId.setter
	def OrgnlPtyAndAcctId(self, value):
		self._OrgnlPtyAndAcctId = value if type(value) != auto else self.make_default("OrgnlPtyAndAcctId")

	@OrgnlPtyAndAcctId.deleter
	def OrgnlPtyAndAcctId(self):
		del self._OrgnlPtyAndAcctId
		self._OrgnlPtyAndAcctId = None

	@property
	def UpdtdPtyAndAcctId(self):
		return self._UpdtdPtyAndAcctId

	@UpdtdPtyAndAcctId.setter
	def UpdtdPtyAndAcctId(self, value):
		self._UpdtdPtyAndAcctId = value if type(value) != auto else self.make_default("UpdtdPtyAndAcctId")

	@UpdtdPtyAndAcctId.deleter
	def UpdtdPtyAndAcctId(self):
		del self._UpdtdPtyAndAcctId
		self._UpdtdPtyAndAcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPtyAndAcctId', type=IdentificationInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdtdPtyAndAcctId', type=IdentificationInformation5, min=1, max=1, mutex_group=None, array=False),
	))

