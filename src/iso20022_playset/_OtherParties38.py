# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification136
from . import PartyIdentification149

class OtherParties38(base_types._BaseFieldType):

	__slots__ = ["_Invstr", "_Issr"]
	@property
	def Invstr(self):
		return self._Invstr

	@Invstr.setter
	def Invstr(self, value):
		self._Invstr = value if value is not None else base_types.UninitialisedField(self, 'Invstr', PartyIdentification149, True)

	@Invstr.deleter
	def Invstr(self):
		del self._Invstr
		self._Invstr = base_types.UninitialisedField(self, 'Invstr', PartyIdentification149, True)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', PartyIdentification136, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', PartyIdentification136, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Invstr', type=PartyIdentification149, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Issr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
	))