import base_types
import Max35Text
import RemittanceLocationData2

class RemittanceLocation8(base_types._BaseFieldType):

	__slots__ = ["_RmtLctnDtls", "_RmtId"]
	@property
	def RmtLctnDtls(self):
		return self._RmtLctnDtls

	@RmtLctnDtls.setter
	def RmtLctnDtls(self, value):
		self._RmtLctnDtls = value if type(value) != auto else self.make_default("RmtLctnDtls")

	@RmtLctnDtls.deleter
	def RmtLctnDtls(self):
		del self._RmtLctnDtls
		self._RmtLctnDtls = None

	@property
	def RmtId(self):
		return self._RmtId

	@RmtId.setter
	def RmtId(self, value):
		self._RmtId = value if type(value) != auto else self.make_default("RmtId")

	@RmtId.deleter
	def RmtId(self):
		del self._RmtId
		self._RmtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RmtLctnDtls', type=RemittanceLocationData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

