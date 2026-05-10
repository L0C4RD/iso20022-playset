from . import base_types
import SecurityAttributes11
import BusinessError4

class SecurityOrBusinessError4Choice(base_types._BaseFieldType):

	__slots__ = ["_SctyRpt", "_BizErr"]
	@property
	def SctyRpt(self):
		return self._SctyRpt

	@SctyRpt.setter
	def SctyRpt(self, value):
		self._SctyRpt = value if type(value) != auto else self.make_default("SctyRpt")

	@SctyRpt.deleter
	def SctyRpt(self):
		del self._SctyRpt
		self._SctyRpt = None

	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyRpt', type=SecurityAttributes11, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='BizErr', type=BusinessError4, min=1, max=None, mutex_group=1, array=True),
	))

