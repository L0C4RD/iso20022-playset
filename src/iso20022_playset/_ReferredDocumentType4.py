# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import ReferredDocumentType3Choice

class ReferredDocumentType4(base_types._BaseFieldType):

	__slots__ = ["_CdOrPrtry", "_Issr"]
	@property
	def CdOrPrtry(self):
		return self._CdOrPrtry

	@CdOrPrtry.setter
	def CdOrPrtry(self, value):
		self._CdOrPrtry = value if value is not None else base_types.UninitialisedField(self, 'CdOrPrtry', ReferredDocumentType3Choice, False)

	@CdOrPrtry.deleter
	def CdOrPrtry(self):
		del self._CdOrPrtry
		self._CdOrPrtry = base_types.UninitialisedField(self, 'CdOrPrtry', ReferredDocumentType3Choice, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', Max35Text, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdOrPrtry', type=ReferredDocumentType3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))