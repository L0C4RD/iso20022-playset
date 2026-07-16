# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionType8Code
from . import Max256Text
from . import Max35Text

class RecommendationAction1(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_Dtls", "_OthrActn"]
	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if value is not None else base_types.UninitialisedField(self, 'Actn', ActionType8Code, False)

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = base_types.UninitialisedField(self, 'Actn', ActionType8Code, False)

	@property
	def Dtls(self):
		return self._Dtls

	@Dtls.setter
	def Dtls(self, value):
		self._Dtls = value if value is not None else base_types.UninitialisedField(self, 'Dtls', Max256Text, True)

	@Dtls.deleter
	def Dtls(self):
		del self._Dtls
		self._Dtls = base_types.UninitialisedField(self, 'Dtls', Max256Text, True)

	@property
	def OthrActn(self):
		return self._OthrActn

	@OthrActn.setter
	def OthrActn(self, value):
		self._OthrActn = value if value is not None else base_types.UninitialisedField(self, 'OthrActn', Max35Text, False)

	@OthrActn.deleter
	def OthrActn(self):
		del self._OthrActn
		self._OthrActn = base_types.UninitialisedField(self, 'OthrActn', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=ActionType8Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dtls', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrActn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))