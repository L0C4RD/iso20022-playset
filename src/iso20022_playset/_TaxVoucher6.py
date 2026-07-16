# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class TaxVoucher6(base_types._BaseFieldType):

	__slots__ = ["_BnfclOwnrRef", "_TaxRclmDcmnttnRef", "_TaxVchrRef"]
	@property
	def BnfclOwnrRef(self):
		return self._BnfclOwnrRef

	@BnfclOwnrRef.setter
	def BnfclOwnrRef(self, value):
		self._BnfclOwnrRef = value if value is not None else base_types.UninitialisedField(self, 'BnfclOwnrRef', Max35Text, False)

	@BnfclOwnrRef.deleter
	def BnfclOwnrRef(self):
		del self._BnfclOwnrRef
		self._BnfclOwnrRef = base_types.UninitialisedField(self, 'BnfclOwnrRef', Max35Text, False)

	@property
	def TaxRclmDcmnttnRef(self):
		return self._TaxRclmDcmnttnRef

	@TaxRclmDcmnttnRef.setter
	def TaxRclmDcmnttnRef(self, value):
		self._TaxRclmDcmnttnRef = value if value is not None else base_types.UninitialisedField(self, 'TaxRclmDcmnttnRef', Max35Text, False)

	@TaxRclmDcmnttnRef.deleter
	def TaxRclmDcmnttnRef(self):
		del self._TaxRclmDcmnttnRef
		self._TaxRclmDcmnttnRef = base_types.UninitialisedField(self, 'TaxRclmDcmnttnRef', Max35Text, False)

	@property
	def TaxVchrRef(self):
		return self._TaxVchrRef

	@TaxVchrRef.setter
	def TaxVchrRef(self, value):
		self._TaxVchrRef = value if value is not None else base_types.UninitialisedField(self, 'TaxVchrRef', Max35Text, False)

	@TaxVchrRef.deleter
	def TaxVchrRef(self):
		del self._TaxVchrRef
		self._TaxVchrRef = base_types.UninitialisedField(self, 'TaxVchrRef', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BnfclOwnrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRclmDcmnttnRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxVchrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))