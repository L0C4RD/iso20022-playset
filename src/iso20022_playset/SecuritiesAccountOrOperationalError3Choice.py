import base_types
import SecuritiesAccountReport3
import ErrorHandling5

class SecuritiesAccountOrOperationalError3Choice(base_types._BaseFieldType):

	__slots__ = ["_SctiesAcctRpt", "_OprlErr"]
	@property
	def SctiesAcctRpt(self):
		return self._SctiesAcctRpt

	@SctiesAcctRpt.setter
	def SctiesAcctRpt(self, value):
		self._SctiesAcctRpt = value if type(value) != auto else self.make_default("SctiesAcctRpt")

	@SctiesAcctRpt.deleter
	def SctiesAcctRpt(self):
		del self._SctiesAcctRpt
		self._SctiesAcctRpt = None

	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if type(value) != auto else self.make_default("OprlErr")

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesAcctRpt', type=SecuritiesAccountReport3, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))

