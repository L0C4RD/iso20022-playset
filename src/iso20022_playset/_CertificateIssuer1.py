# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RelativeDistinguishedName1

class CertificateIssuer1(base_types._BaseFieldType):

	__slots__ = ["_RltvDstngshdNm"]
	@property
	def RltvDstngshdNm(self):
		return self._RltvDstngshdNm

	@RltvDstngshdNm.setter
	def RltvDstngshdNm(self, value):
		self._RltvDstngshdNm = value if value is not None else base_types.UninitialisedField(self, 'RltvDstngshdNm', RelativeDistinguishedName1, True)

	@RltvDstngshdNm.deleter
	def RltvDstngshdNm(self):
		del self._RltvDstngshdNm
		self._RltvDstngshdNm = base_types.UninitialisedField(self, 'RltvDstngshdNm', RelativeDistinguishedName1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltvDstngshdNm', type=RelativeDistinguishedName1, min=1, max=None, mutex_group=None, array=True),
	))