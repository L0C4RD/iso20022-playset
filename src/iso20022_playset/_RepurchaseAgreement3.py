# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LEIIdentifier
from . import ProductClassification1
from . import RepurchaseAgreementType1Choice

class RepurchaseAgreement3(base_types._BaseFieldType):

	__slots__ = ["_PdctClssfctn", "_RpAgrmtTp", "_TrptyAgt"]
	@property
	def PdctClssfctn(self):
		return self._PdctClssfctn

	@PdctClssfctn.setter
	def PdctClssfctn(self, value):
		self._PdctClssfctn = value if value is not None else base_types.UninitialisedField(self, 'PdctClssfctn', ProductClassification1, False)

	@PdctClssfctn.deleter
	def PdctClssfctn(self):
		del self._PdctClssfctn
		self._PdctClssfctn = base_types.UninitialisedField(self, 'PdctClssfctn', ProductClassification1, False)

	@property
	def RpAgrmtTp(self):
		return self._RpAgrmtTp

	@RpAgrmtTp.setter
	def RpAgrmtTp(self, value):
		self._RpAgrmtTp = value if value is not None else base_types.UninitialisedField(self, 'RpAgrmtTp', RepurchaseAgreementType1Choice, False)

	@RpAgrmtTp.deleter
	def RpAgrmtTp(self):
		del self._RpAgrmtTp
		self._RpAgrmtTp = base_types.UninitialisedField(self, 'RpAgrmtTp', RepurchaseAgreementType1Choice, False)

	@property
	def TrptyAgt(self):
		return self._TrptyAgt

	@TrptyAgt.setter
	def TrptyAgt(self, value):
		self._TrptyAgt = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgt', LEIIdentifier, False)

	@TrptyAgt.deleter
	def TrptyAgt(self):
		del self._TrptyAgt
		self._TrptyAgt = base_types.UninitialisedField(self, 'TrptyAgt', LEIIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdctClssfctn', type=ProductClassification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpAgrmtTp', type=RepurchaseAgreementType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgt', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))