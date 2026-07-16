# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import EmploymentDetails1

class Drawdown3(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_MplymntDtls"]
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
	def MplymntDtls(self):
		return self._MplymntDtls

	@MplymntDtls.setter
	def MplymntDtls(self, value):
		self._MplymntDtls = value if value is not None else base_types.UninitialisedField(self, 'MplymntDtls', EmploymentDetails1, False)

	@MplymntDtls.deleter
	def MplymntDtls(self):
		del self._MplymntDtls
		self._MplymntDtls = base_types.UninitialisedField(self, 'MplymntDtls', EmploymentDetails1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MplymntDtls', type=EmploymentDetails1, min=0, max=1, mutex_group=None, array=False),
	))