# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max140Text

class TechnicalAttributes6(base_types._BaseFieldType):

	__slots__ = ["_RptRctTmStmp", "_TechRcrdId"]
	@property
	def RptRctTmStmp(self):
		return self._RptRctTmStmp

	@RptRctTmStmp.setter
	def RptRctTmStmp(self, value):
		self._RptRctTmStmp = value if value is not None else base_types.UninitialisedField(self, 'RptRctTmStmp', ISODateTime, False)

	@RptRctTmStmp.deleter
	def RptRctTmStmp(self):
		del self._RptRctTmStmp
		self._RptRctTmStmp = base_types.UninitialisedField(self, 'RptRctTmStmp', ISODateTime, False)

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max140Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptRctTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))