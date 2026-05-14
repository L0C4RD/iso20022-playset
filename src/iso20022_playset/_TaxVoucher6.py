from . import base_types
from ._Max35Text import Max35Text

class TaxVoucher6(base_types._BaseFieldType):

	__slots__ = ["_BnfclOwnrRef", "_TaxRclmDcmnttnRef", "_TaxVchrRef"]
	@property
	def BnfclOwnrRef(self):
		return self._BnfclOwnrRef

	@BnfclOwnrRef.setter
	def BnfclOwnrRef(self, value):
		self._BnfclOwnrRef = value if type(value) != base_types.auto else self.make_default("BnfclOwnrRef")

	@BnfclOwnrRef.deleter
	def BnfclOwnrRef(self):
		del self._BnfclOwnrRef
		self._BnfclOwnrRef = None

	@property
	def TaxRclmDcmnttnRef(self):
		return self._TaxRclmDcmnttnRef

	@TaxRclmDcmnttnRef.setter
	def TaxRclmDcmnttnRef(self, value):
		self._TaxRclmDcmnttnRef = value if type(value) != base_types.auto else self.make_default("TaxRclmDcmnttnRef")

	@TaxRclmDcmnttnRef.deleter
	def TaxRclmDcmnttnRef(self):
		del self._TaxRclmDcmnttnRef
		self._TaxRclmDcmnttnRef = None

	@property
	def TaxVchrRef(self):
		return self._TaxVchrRef

	@TaxVchrRef.setter
	def TaxVchrRef(self, value):
		self._TaxVchrRef = value if type(value) != base_types.auto else self.make_default("TaxVchrRef")

	@TaxVchrRef.deleter
	def TaxVchrRef(self):
		del self._TaxVchrRef
		self._TaxVchrRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BnfclOwnrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRclmDcmnttnRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxVchrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

