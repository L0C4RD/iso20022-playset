# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RelativeDistinguishedName1 import RelativeDistinguishedName1

class CertificateIssuer1(base_types._BaseFieldType):

	__slots__ = ["_RltvDstngshdNm"]
	@property
	def RltvDstngshdNm(self):
		return self._RltvDstngshdNm

	@RltvDstngshdNm.setter
	def RltvDstngshdNm(self, value):
		self._RltvDstngshdNm = value if type(value) != base_types.auto else self.make_default("RltvDstngshdNm")

	@RltvDstngshdNm.deleter
	def RltvDstngshdNm(self):
		del self._RltvDstngshdNm
		self._RltvDstngshdNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltvDstngshdNm', type=RelativeDistinguishedName1, min=1, max=None, mutex_group=None, array=True),
	))