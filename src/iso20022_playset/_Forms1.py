# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SignatureType1Code
from . import YesNoIndicator

class Forms1(base_types._BaseFieldType):

	__slots__ = ["_ApplForm", "_SgntrTp"]
	@property
	def ApplForm(self):
		return self._ApplForm

	@ApplForm.setter
	def ApplForm(self, value):
		self._ApplForm = value if value is not None else base_types.UninitialisedField(self, 'ApplForm', YesNoIndicator, False)

	@ApplForm.deleter
	def ApplForm(self):
		del self._ApplForm
		self._ApplForm = base_types.UninitialisedField(self, 'ApplForm', YesNoIndicator, False)

	@property
	def SgntrTp(self):
		return self._SgntrTp

	@SgntrTp.setter
	def SgntrTp(self, value):
		self._SgntrTp = value if value is not None else base_types.UninitialisedField(self, 'SgntrTp', SignatureType1Code, False)

	@SgntrTp.deleter
	def SgntrTp(self):
		del self._SgntrTp
		self._SgntrTp = base_types.UninitialisedField(self, 'SgntrTp', SignatureType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApplForm', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrTp', type=SignatureType1Code, min=1, max=1, mutex_group=None, array=False),
	))