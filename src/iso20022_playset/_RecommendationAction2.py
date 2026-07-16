# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max256Text
from . import RecommendedActionCode1

class RecommendationAction2(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_Dtls"]
	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if value is not None else base_types.UninitialisedField(self, 'Actn', RecommendedActionCode1, False)

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = base_types.UninitialisedField(self, 'Actn', RecommendedActionCode1, False)

	@property
	def Dtls(self):
		return self._Dtls

	@Dtls.setter
	def Dtls(self, value):
		self._Dtls = value if value is not None else base_types.UninitialisedField(self, 'Dtls', Max256Text, False)

	@Dtls.deleter
	def Dtls(self):
		del self._Dtls
		self._Dtls = base_types.UninitialisedField(self, 'Dtls', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=RecommendedActionCode1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dtls', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))