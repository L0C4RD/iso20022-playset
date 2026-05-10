from . import base_types
from .OriginalPaymentInstruction49 import OriginalPaymentInstruction49
from .OriginalGroupHeader21 import OriginalGroupHeader21

class UnderlyingTransaction33(base_types._BaseFieldType):

	__slots__ = ["_OrgnlPmtInfAndCxl", "_OrgnlGrpInfAndCxl"]
	@property
	def OrgnlPmtInfAndCxl(self):
		return self._OrgnlPmtInfAndCxl

	@OrgnlPmtInfAndCxl.setter
	def OrgnlPmtInfAndCxl(self, value):
		self._OrgnlPmtInfAndCxl = value if type(value) != auto else self.make_default("OrgnlPmtInfAndCxl")

	@OrgnlPmtInfAndCxl.deleter
	def OrgnlPmtInfAndCxl(self):
		del self._OrgnlPmtInfAndCxl
		self._OrgnlPmtInfAndCxl = None

	@property
	def OrgnlGrpInfAndCxl(self):
		return self._OrgnlGrpInfAndCxl

	@OrgnlGrpInfAndCxl.setter
	def OrgnlGrpInfAndCxl(self, value):
		self._OrgnlGrpInfAndCxl = value if type(value) != auto else self.make_default("OrgnlGrpInfAndCxl")

	@OrgnlGrpInfAndCxl.deleter
	def OrgnlGrpInfAndCxl(self):
		del self._OrgnlGrpInfAndCxl
		self._OrgnlGrpInfAndCxl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlPmtInfAndCxl', type=OriginalPaymentInstruction49, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlGrpInfAndCxl', type=OriginalGroupHeader21, min=0, max=1, mutex_group=None, array=False),
	))

