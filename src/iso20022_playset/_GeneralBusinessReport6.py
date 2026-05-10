from . import base_types
from .Max35Text import Max35Text
from .GeneralBusinessOrError8Choice import GeneralBusinessOrError8Choice

class GeneralBusinessReport6(base_types._BaseFieldType):

	__slots__ = ["_BizInfRef", "_GnlBizOrErr"]
	@property
	def BizInfRef(self):
		return self._BizInfRef

	@BizInfRef.setter
	def BizInfRef(self, value):
		self._BizInfRef = value if type(value) != base_types.auto else self.make_default("BizInfRef")

	@BizInfRef.deleter
	def BizInfRef(self):
		del self._BizInfRef
		self._BizInfRef = None

	@property
	def GnlBizOrErr(self):
		return self._GnlBizOrErr

	@GnlBizOrErr.setter
	def GnlBizOrErr(self, value):
		self._GnlBizOrErr = value if type(value) != base_types.auto else self.make_default("GnlBizOrErr")

	@GnlBizOrErr.deleter
	def GnlBizOrErr(self):
		del self._GnlBizOrErr
		self._GnlBizOrErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizInfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlBizOrErr', type=GeneralBusinessOrError8Choice, min=1, max=1, mutex_group=None, array=False),
	))

