# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import TaxReferenceParty1Choice
from . import TaxReferenceType1Choice

class TaxReference1(base_types._BaseFieldType):

	__slots__ = ["_HldrTp", "_Ref", "_TaxTp"]
	@property
	def HldrTp(self):
		return self._HldrTp

	@HldrTp.setter
	def HldrTp(self, value):
		self._HldrTp = value if value is not None else base_types.UninitialisedField(self, 'HldrTp', TaxReferenceParty1Choice, False)

	@HldrTp.deleter
	def HldrTp(self):
		del self._HldrTp
		self._HldrTp = base_types.UninitialisedField(self, 'HldrTp', TaxReferenceParty1Choice, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@property
	def TaxTp(self):
		return self._TaxTp

	@TaxTp.setter
	def TaxTp(self, value):
		self._TaxTp = value if value is not None else base_types.UninitialisedField(self, 'TaxTp', TaxReferenceType1Choice, False)

	@TaxTp.deleter
	def TaxTp(self):
		del self._TaxTp
		self._TaxTp = base_types.UninitialisedField(self, 'TaxTp', TaxReferenceType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HldrTp', type=TaxReferenceParty1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxTp', type=TaxReferenceType1Choice, min=0, max=1, mutex_group=None, array=False),
	))