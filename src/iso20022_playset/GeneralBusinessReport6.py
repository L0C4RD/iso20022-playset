from . import base_types
import GeneralBusinessOrError8Choice
import Max35Text

class GeneralBusinessReport6(base_types._BaseFieldType):

	__slots__ = ["_GnlBizOrErr", "_BizInfRef"]
	@property
	def GnlBizOrErr(self):
		return self._GnlBizOrErr

	@GnlBizOrErr.setter
	def GnlBizOrErr(self, value):
		self._GnlBizOrErr = value if type(value) != auto else self.make_default("GnlBizOrErr")

	@GnlBizOrErr.deleter
	def GnlBizOrErr(self):
		del self._GnlBizOrErr
		self._GnlBizOrErr = None

	@property
	def BizInfRef(self):
		return self._BizInfRef

	@BizInfRef.setter
	def BizInfRef(self, value):
		self._BizInfRef = value if type(value) != auto else self.make_default("BizInfRef")

	@BizInfRef.deleter
	def BizInfRef(self):
		del self._BizInfRef
		self._BizInfRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GnlBizOrErr', type=GeneralBusinessOrError8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizInfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

