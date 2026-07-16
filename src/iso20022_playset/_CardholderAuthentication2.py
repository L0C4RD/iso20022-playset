# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthenticationEntity1Code
from . import AuthenticationMethod1Code

class CardholderAuthentication2(base_types._BaseFieldType):

	__slots__ = ["_AuthntcnMtd", "_AuthntcnNtty"]
	@property
	def AuthntcnMtd(self):
		return self._AuthntcnMtd

	@AuthntcnMtd.setter
	def AuthntcnMtd(self, value):
		self._AuthntcnMtd = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnMtd', AuthenticationMethod1Code, False)

	@AuthntcnMtd.deleter
	def AuthntcnMtd(self):
		del self._AuthntcnMtd
		self._AuthntcnMtd = base_types.UninitialisedField(self, 'AuthntcnMtd', AuthenticationMethod1Code, False)

	@property
	def AuthntcnNtty(self):
		return self._AuthntcnNtty

	@AuthntcnNtty.setter
	def AuthntcnNtty(self, value):
		self._AuthntcnNtty = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnNtty', AuthenticationEntity1Code, False)

	@AuthntcnNtty.deleter
	def AuthntcnNtty(self):
		del self._AuthntcnNtty
		self._AuthntcnNtty = base_types.UninitialisedField(self, 'AuthntcnNtty', AuthenticationEntity1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthntcnMtd', type=AuthenticationMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnNtty', type=AuthenticationEntity1Code, min=1, max=1, mutex_group=None, array=False),
	))