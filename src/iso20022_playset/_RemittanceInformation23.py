# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import Max35Text
from . import OriginalPaymentInformation10
from . import StructuredRemittanceInformation18

class RemittanceInformation23(base_types._BaseFieldType):

	__slots__ = ["_OrgnlPmtInf", "_RmtId", "_Strd", "_Ustrd"]
	@property
	def OrgnlPmtInf(self):
		return self._OrgnlPmtInf

	@OrgnlPmtInf.setter
	def OrgnlPmtInf(self, value):
		self._OrgnlPmtInf = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPmtInf', OriginalPaymentInformation10, False)

	@OrgnlPmtInf.deleter
	def OrgnlPmtInf(self):
		del self._OrgnlPmtInf
		self._OrgnlPmtInf = base_types.UninitialisedField(self, 'OrgnlPmtInf', OriginalPaymentInformation10, False)

	@property
	def RmtId(self):
		return self._RmtId

	@RmtId.setter
	def RmtId(self, value):
		self._RmtId = value if value is not None else base_types.UninitialisedField(self, 'RmtId', Max35Text, False)

	@RmtId.deleter
	def RmtId(self):
		del self._RmtId
		self._RmtId = base_types.UninitialisedField(self, 'RmtId', Max35Text, False)

	@property
	def Strd(self):
		return self._Strd

	@Strd.setter
	def Strd(self, value):
		self._Strd = value if value is not None else base_types.UninitialisedField(self, 'Strd', StructuredRemittanceInformation18, True)

	@Strd.deleter
	def Strd(self):
		del self._Strd
		self._Strd = base_types.UninitialisedField(self, 'Strd', StructuredRemittanceInformation18, True)

	@property
	def Ustrd(self):
		return self._Ustrd

	@Ustrd.setter
	def Ustrd(self, value):
		self._Ustrd = value if value is not None else base_types.UninitialisedField(self, 'Ustrd', Max140Text, True)

	@Ustrd.deleter
	def Ustrd(self):
		del self._Ustrd
		self._Ustrd = base_types.UninitialisedField(self, 'Ustrd', Max140Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlPmtInf', type=OriginalPaymentInformation10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Strd', type=StructuredRemittanceInformation18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ustrd', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
	))