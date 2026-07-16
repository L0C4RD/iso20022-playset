# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BillingTaxCalculationMethod1Code
from . import Max40Text
from . import ResidenceLocation1Choice

class AccountTax1(base_types._BaseFieldType):

	__slots__ = ["_ClctnMtd", "_NonResCtry", "_Rgn"]
	@property
	def ClctnMtd(self):
		return self._ClctnMtd

	@ClctnMtd.setter
	def ClctnMtd(self, value):
		self._ClctnMtd = value if value is not None else base_types.UninitialisedField(self, 'ClctnMtd', BillingTaxCalculationMethod1Code, False)

	@ClctnMtd.deleter
	def ClctnMtd(self):
		del self._ClctnMtd
		self._ClctnMtd = base_types.UninitialisedField(self, 'ClctnMtd', BillingTaxCalculationMethod1Code, False)

	@property
	def NonResCtry(self):
		return self._NonResCtry

	@NonResCtry.setter
	def NonResCtry(self, value):
		self._NonResCtry = value if value is not None else base_types.UninitialisedField(self, 'NonResCtry', ResidenceLocation1Choice, False)

	@NonResCtry.deleter
	def NonResCtry(self):
		del self._NonResCtry
		self._NonResCtry = base_types.UninitialisedField(self, 'NonResCtry', ResidenceLocation1Choice, False)

	@property
	def Rgn(self):
		return self._Rgn

	@Rgn.setter
	def Rgn(self, value):
		self._Rgn = value if value is not None else base_types.UninitialisedField(self, 'Rgn', Max40Text, False)

	@Rgn.deleter
	def Rgn(self):
		del self._Rgn
		self._Rgn = base_types.UninitialisedField(self, 'Rgn', Max40Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClctnMtd', type=BillingTaxCalculationMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonResCtry', type=ResidenceLocation1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rgn', type=Max40Text, min=0, max=1, mutex_group=None, array=False),
	))