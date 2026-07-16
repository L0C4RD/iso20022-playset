# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max4AlphaNumericText
from . import RestrictedFINXMax30Text

class SecuritiesCertificate5(base_types._BaseFieldType):

	__slots__ = ["_Issr", "_Nb", "_SchmeNm"]
	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', Max4AlphaNumericText, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', Max4AlphaNumericText, False)

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if value is not None else base_types.UninitialisedField(self, 'Nb', RestrictedFINXMax30Text, False)

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = base_types.UninitialisedField(self, 'Nb', RestrictedFINXMax30Text, False)

	@property
	def SchmeNm(self):
		return self._SchmeNm

	@SchmeNm.setter
	def SchmeNm(self, value):
		self._SchmeNm = value if value is not None else base_types.UninitialisedField(self, 'SchmeNm', Max4AlphaNumericText, False)

	@SchmeNm.deleter
	def SchmeNm(self):
		del self._SchmeNm
		self._SchmeNm = base_types.UninitialisedField(self, 'SchmeNm', Max4AlphaNumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Issr', type=Max4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=RestrictedFINXMax30Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchmeNm', type=Max4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))