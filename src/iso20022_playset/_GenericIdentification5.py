# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact4AlphaNumericText
from . import Max35Text
from . import Max8Text

class GenericIdentification5(base_types._BaseFieldType):

	__slots__ = ["_Inf", "_Issr", "_Nrrtv"]
	@property
	def Inf(self):
		return self._Inf

	@Inf.setter
	def Inf(self, value):
		self._Inf = value if value is not None else base_types.UninitialisedField(self, 'Inf', Exact4AlphaNumericText, False)

	@Inf.deleter
	def Inf(self):
		del self._Inf
		self._Inf = base_types.UninitialisedField(self, 'Inf', Exact4AlphaNumericText, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', Max8Text, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', Max8Text, False)

	@property
	def Nrrtv(self):
		return self._Nrrtv

	@Nrrtv.setter
	def Nrrtv(self, value):
		self._Nrrtv = value if value is not None else base_types.UninitialisedField(self, 'Nrrtv', Max35Text, False)

	@Nrrtv.deleter
	def Nrrtv(self):
		del self._Nrrtv
		self._Nrrtv = base_types.UninitialisedField(self, 'Nrrtv', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Inf', type=Exact4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=Max8Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nrrtv', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))