# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max256Text
from . import Max350Text

class AgreementClauses1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_DocURL"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max256Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max256Text, False)

	@property
	def DocURL(self):
		return self._DocURL

	@DocURL.setter
	def DocURL(self, value):
		self._DocURL = value if value is not None else base_types.UninitialisedField(self, 'DocURL', Max350Text, False)

	@DocURL.deleter
	def DocURL(self):
		del self._DocURL
		self._DocURL = base_types.UninitialisedField(self, 'DocURL', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocURL', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))