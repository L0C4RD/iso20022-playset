from . import base_types
from ._TaxReferenceParty1Choice import TaxReferenceParty1Choice
from ._TaxReferenceType1Choice import TaxReferenceType1Choice
from ._Max35Text import Max35Text

class TaxReference1(base_types._BaseFieldType):

	__slots__ = ["_HldrTp", "_Ref", "_TaxTp"]
	@property
	def HldrTp(self):
		return self._HldrTp

	@HldrTp.setter
	def HldrTp(self, value):
		self._HldrTp = value if type(value) != base_types.auto else self.make_default("HldrTp")

	@HldrTp.deleter
	def HldrTp(self):
		del self._HldrTp
		self._HldrTp = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def TaxTp(self):
		return self._TaxTp

	@TaxTp.setter
	def TaxTp(self, value):
		self._TaxTp = value if type(value) != base_types.auto else self.make_default("TaxTp")

	@TaxTp.deleter
	def TaxTp(self):
		del self._TaxTp
		self._TaxTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HldrTp', type=TaxReferenceParty1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxTp', type=TaxReferenceType1Choice, min=0, max=1, mutex_group=None, array=False),
	))

