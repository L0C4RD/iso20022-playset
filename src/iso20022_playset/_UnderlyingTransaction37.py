# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OriginalGroupHeader21
from . import OriginalPaymentInstruction55

class UnderlyingTransaction37(base_types._BaseFieldType):

	__slots__ = ["_OrgnlGrpInfAndCxl", "_OrgnlPmtInfAndCxl"]
	@property
	def OrgnlGrpInfAndCxl(self):
		return self._OrgnlGrpInfAndCxl

	@OrgnlGrpInfAndCxl.setter
	def OrgnlGrpInfAndCxl(self, value):
		self._OrgnlGrpInfAndCxl = value if value is not None else base_types.UninitialisedField(self, 'OrgnlGrpInfAndCxl', OriginalGroupHeader21, False)

	@OrgnlGrpInfAndCxl.deleter
	def OrgnlGrpInfAndCxl(self):
		del self._OrgnlGrpInfAndCxl
		self._OrgnlGrpInfAndCxl = base_types.UninitialisedField(self, 'OrgnlGrpInfAndCxl', OriginalGroupHeader21, False)

	@property
	def OrgnlPmtInfAndCxl(self):
		return self._OrgnlPmtInfAndCxl

	@OrgnlPmtInfAndCxl.setter
	def OrgnlPmtInfAndCxl(self, value):
		self._OrgnlPmtInfAndCxl = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPmtInfAndCxl', OriginalPaymentInstruction55, True)

	@OrgnlPmtInfAndCxl.deleter
	def OrgnlPmtInfAndCxl(self):
		del self._OrgnlPmtInfAndCxl
		self._OrgnlPmtInfAndCxl = base_types.UninitialisedField(self, 'OrgnlPmtInfAndCxl', OriginalPaymentInstruction55, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlGrpInfAndCxl', type=OriginalGroupHeader21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtInfAndCxl', type=OriginalPaymentInstruction55, min=0, max=None, mutex_group=None, array=True),
	))