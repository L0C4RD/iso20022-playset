from . import base_types
import Max35Text

class AccountIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_SctiesAcctId", "_CshAcctId"]
	@property
	def SctiesAcctId(self):
		return self._SctiesAcctId

	@SctiesAcctId.setter
	def SctiesAcctId(self, value):
		self._SctiesAcctId = value if type(value) != auto else self.make_default("SctiesAcctId")

	@SctiesAcctId.deleter
	def SctiesAcctId(self):
		del self._SctiesAcctId
		self._SctiesAcctId = None

	@property
	def CshAcctId(self):
		return self._CshAcctId

	@CshAcctId.setter
	def CshAcctId(self, value):
		self._CshAcctId = value if type(value) != auto else self.make_default("CshAcctId")

	@CshAcctId.deleter
	def CshAcctId(self):
		del self._CshAcctId
		self._CshAcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesAcctId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshAcctId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

