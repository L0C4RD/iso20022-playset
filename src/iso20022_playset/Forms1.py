from . import base_types
import YesNoIndicator
import SignatureType1Code

class Forms1(base_types._BaseFieldType):

	__slots__ = ["_ApplForm", "_SgntrTp"]
	@property
	def ApplForm(self):
		return self._ApplForm

	@ApplForm.setter
	def ApplForm(self, value):
		self._ApplForm = value if type(value) != auto else self.make_default("ApplForm")

	@ApplForm.deleter
	def ApplForm(self):
		del self._ApplForm
		self._ApplForm = None

	@property
	def SgntrTp(self):
		return self._SgntrTp

	@SgntrTp.setter
	def SgntrTp(self, value):
		self._SgntrTp = value if type(value) != auto else self.make_default("SgntrTp")

	@SgntrTp.deleter
	def SgntrTp(self):
		del self._SgntrTp
		self._SgntrTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApplForm', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrTp', type=SignatureType1Code, min=1, max=1, mutex_group=None, array=False),
	))

