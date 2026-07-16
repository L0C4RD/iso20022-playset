# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification36
from . import Max350Text

class InnovativeFinance1(base_types._BaseFieldType):

	__slots__ = ["_Inf", "_Tp"]
	@property
	def Inf(self):
		return self._Inf

	@Inf.setter
	def Inf(self, value):
		self._Inf = value if value is not None else base_types.UninitialisedField(self, 'Inf', Max350Text, False)

	@Inf.deleter
	def Inf(self):
		del self._Inf
		self._Inf = base_types.UninitialisedField(self, 'Inf', Max350Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', GenericIdentification36, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', GenericIdentification36, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Inf', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=GenericIdentification36, min=1, max=1, mutex_group=None, array=False),
	))