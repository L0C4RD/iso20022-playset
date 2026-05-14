# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LEIIdentifier import LEIIdentifier
from ._ProductClassification1 import ProductClassification1
from ._RepurchaseAgreementType1Choice import RepurchaseAgreementType1Choice

class RepurchaseAgreement3(base_types._BaseFieldType):

	__slots__ = ["_PdctClssfctn", "_RpAgrmtTp", "_TrptyAgt"]
	@property
	def PdctClssfctn(self):
		return self._PdctClssfctn

	@PdctClssfctn.setter
	def PdctClssfctn(self, value):
		self._PdctClssfctn = value if type(value) != base_types.auto else self.make_default("PdctClssfctn")

	@PdctClssfctn.deleter
	def PdctClssfctn(self):
		del self._PdctClssfctn
		self._PdctClssfctn = None

	@property
	def RpAgrmtTp(self):
		return self._RpAgrmtTp

	@RpAgrmtTp.setter
	def RpAgrmtTp(self, value):
		self._RpAgrmtTp = value if type(value) != base_types.auto else self.make_default("RpAgrmtTp")

	@RpAgrmtTp.deleter
	def RpAgrmtTp(self):
		del self._RpAgrmtTp
		self._RpAgrmtTp = None

	@property
	def TrptyAgt(self):
		return self._TrptyAgt

	@TrptyAgt.setter
	def TrptyAgt(self, value):
		self._TrptyAgt = value if type(value) != base_types.auto else self.make_default("TrptyAgt")

	@TrptyAgt.deleter
	def TrptyAgt(self):
		del self._TrptyAgt
		self._TrptyAgt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdctClssfctn', type=ProductClassification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpAgrmtTp', type=RepurchaseAgreementType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgt', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))