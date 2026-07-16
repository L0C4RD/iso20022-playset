# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max15NumericText
from . import RejectionReason45

class NumberOfTransactionsPerValidationRule5(base_types._BaseFieldType):

	__slots__ = ["_DtldNb", "_RptSts"]
	@property
	def DtldNb(self):
		return self._DtldNb

	@DtldNb.setter
	def DtldNb(self, value):
		self._DtldNb = value if value is not None else base_types.UninitialisedField(self, 'DtldNb', Max15NumericText, False)

	@DtldNb.deleter
	def DtldNb(self):
		del self._DtldNb
		self._DtldNb = base_types.UninitialisedField(self, 'DtldNb', Max15NumericText, False)

	@property
	def RptSts(self):
		return self._RptSts

	@RptSts.setter
	def RptSts(self, value):
		self._RptSts = value if value is not None else base_types.UninitialisedField(self, 'RptSts', RejectionReason45, True)

	@RptSts.deleter
	def RptSts(self):
		del self._RptSts
		self._RptSts = base_types.UninitialisedField(self, 'RptSts', RejectionReason45, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldNb', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSts', type=RejectionReason45, min=1, max=None, mutex_group=None, array=True),
	))