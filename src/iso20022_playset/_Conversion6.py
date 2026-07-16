# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import FinancialInstrumentIdentification7

class Conversion6(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_OrgnlScty"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def OrgnlScty(self):
		return self._OrgnlScty

	@OrgnlScty.setter
	def OrgnlScty(self, value):
		self._OrgnlScty = value if value is not None else base_types.UninitialisedField(self, 'OrgnlScty', FinancialInstrumentIdentification7, False)

	@OrgnlScty.deleter
	def OrgnlScty(self):
		del self._OrgnlScty
		self._OrgnlScty = base_types.UninitialisedField(self, 'OrgnlScty', FinancialInstrumentIdentification7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlScty', type=FinancialInstrumentIdentification7, min=1, max=1, mutex_group=None, array=False),
	))