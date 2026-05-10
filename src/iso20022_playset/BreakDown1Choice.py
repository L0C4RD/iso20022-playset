import base_types
import ReportLine5
import ReportLine6

class BreakDown1Choice(base_types._BaseFieldType):

	__slots__ = ["_ByPurchsOrdr", "_ByComrclInvc"]
	@property
	def ByPurchsOrdr(self):
		return self._ByPurchsOrdr

	@ByPurchsOrdr.setter
	def ByPurchsOrdr(self, value):
		self._ByPurchsOrdr = value if type(value) != auto else self.make_default("ByPurchsOrdr")

	@ByPurchsOrdr.deleter
	def ByPurchsOrdr(self):
		del self._ByPurchsOrdr
		self._ByPurchsOrdr = None

	@property
	def ByComrclInvc(self):
		return self._ByComrclInvc

	@ByComrclInvc.setter
	def ByComrclInvc(self, value):
		self._ByComrclInvc = value if type(value) != auto else self.make_default("ByComrclInvc")

	@ByComrclInvc.deleter
	def ByComrclInvc(self):
		del self._ByComrclInvc
		self._ByComrclInvc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ByPurchsOrdr', type=ReportLine5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ByComrclInvc', type=ReportLine6, min=0, max=1, mutex_group=1, array=False),
	))

