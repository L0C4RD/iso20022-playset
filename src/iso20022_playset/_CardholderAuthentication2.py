# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AuthenticationEntity1Code import AuthenticationEntity1Code
from ._AuthenticationMethod1Code import AuthenticationMethod1Code

class CardholderAuthentication2(base_types._BaseFieldType):

	__slots__ = ["_AuthntcnMtd", "_AuthntcnNtty"]
	@property
	def AuthntcnMtd(self):
		return self._AuthntcnMtd

	@AuthntcnMtd.setter
	def AuthntcnMtd(self, value):
		self._AuthntcnMtd = value if type(value) != base_types.auto else self.make_default("AuthntcnMtd")

	@AuthntcnMtd.deleter
	def AuthntcnMtd(self):
		del self._AuthntcnMtd
		self._AuthntcnMtd = None

	@property
	def AuthntcnNtty(self):
		return self._AuthntcnNtty

	@AuthntcnNtty.setter
	def AuthntcnNtty(self, value):
		self._AuthntcnNtty = value if type(value) != base_types.auto else self.make_default("AuthntcnNtty")

	@AuthntcnNtty.deleter
	def AuthntcnNtty(self):
		del self._AuthntcnNtty
		self._AuthntcnNtty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthntcnMtd', type=AuthenticationMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnNtty', type=AuthenticationEntity1Code, min=1, max=1, mutex_group=None, array=False),
	))