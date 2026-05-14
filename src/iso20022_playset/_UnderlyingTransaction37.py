# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._OriginalGroupHeader21 import OriginalGroupHeader21
from ._OriginalPaymentInstruction55 import OriginalPaymentInstruction55

class UnderlyingTransaction37(base_types._BaseFieldType):

	__slots__ = ["_OrgnlGrpInfAndCxl", "_OrgnlPmtInfAndCxl"]
	@property
	def OrgnlGrpInfAndCxl(self):
		return self._OrgnlGrpInfAndCxl

	@OrgnlGrpInfAndCxl.setter
	def OrgnlGrpInfAndCxl(self, value):
		self._OrgnlGrpInfAndCxl = value if type(value) != base_types.auto else self.make_default("OrgnlGrpInfAndCxl")

	@OrgnlGrpInfAndCxl.deleter
	def OrgnlGrpInfAndCxl(self):
		del self._OrgnlGrpInfAndCxl
		self._OrgnlGrpInfAndCxl = None

	@property
	def OrgnlPmtInfAndCxl(self):
		return self._OrgnlPmtInfAndCxl

	@OrgnlPmtInfAndCxl.setter
	def OrgnlPmtInfAndCxl(self, value):
		self._OrgnlPmtInfAndCxl = value if type(value) != base_types.auto else self.make_default("OrgnlPmtInfAndCxl")

	@OrgnlPmtInfAndCxl.deleter
	def OrgnlPmtInfAndCxl(self):
		del self._OrgnlPmtInfAndCxl
		self._OrgnlPmtInfAndCxl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlGrpInfAndCxl', type=OriginalGroupHeader21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtInfAndCxl', type=OriginalPaymentInstruction55, min=0, max=None, mutex_group=None, array=True),
	))