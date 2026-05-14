# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max256Text import Max256Text
from ._Max350Text import Max350Text

class AgreementClauses1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_DocURL"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def DocURL(self):
		return self._DocURL

	@DocURL.setter
	def DocURL(self, value):
		self._DocURL = value if type(value) != base_types.auto else self.make_default("DocURL")

	@DocURL.deleter
	def DocURL(self):
		del self._DocURL
		self._DocURL = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocURL', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))