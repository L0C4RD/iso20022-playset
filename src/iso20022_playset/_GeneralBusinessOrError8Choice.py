from . import base_types
from ._GeneralBusinessInformation1 import GeneralBusinessInformation1
from ._ErrorHandling5 import ErrorHandling5

class GeneralBusinessOrError8Choice(base_types._BaseFieldType):

	__slots__ = ["_GnlBiz", "_BizErr"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != base_types.auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	@property
	def GnlBiz(self):
		return self._GnlBiz

	@GnlBiz.setter
	def GnlBiz(self, value):
		self._GnlBiz = value if type(value) != base_types.auto else self.make_default("GnlBiz")

	@GnlBiz.deleter
	def GnlBiz(self):
		del self._GnlBiz
		self._GnlBiz = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='GnlBiz', type=GeneralBusinessInformation1, min=0, max=1, mutex_group=1, array=False),
	))

